%global packname  betareg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Beta Regression

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-Formula 
Requires:         R-graphics R-flexmix R-lmtest R-methods R-modeltools R-sandwich 

BuildRequires:    R-devel tex(latex) R-stats R-Formula
BuildRequires:    R-graphics R-flexmix R-lmtest R-methods R-modeltools R-sandwich 


%description
Beta regression for modeling beta-distributed dependent variables, e.g.,
rates and proportions.  In addition to maximum likelihood regression (for
both mean and precision of a beta-distributed response), bias-corrected
and bias-reduced estimation as well as finite mixture models and recursive
partitioning for beta regressions are provided.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/betareg/CITATION
%doc %{rlibdir}/betareg/DESCRIPTION
%doc %{rlibdir}/betareg/doc
%doc %{rlibdir}/betareg/html
%doc %{rlibdir}/betareg/NEWS
%{rlibdir}/betareg/help
%{rlibdir}/betareg/Meta
%{rlibdir}/betareg/data
%{rlibdir}/betareg/INDEX
%{rlibdir}/betareg/R
%{rlibdir}/betareg/demo
%{rlibdir}/betareg/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.0-1
- initial package for Fedora