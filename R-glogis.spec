%global packname  glogis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Fitting and Testing Generalized Logistic Distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-zoo 
Requires:         R-graphics R-stats R-sandwich R-zoo 

BuildRequires:    R-devel tex(latex) R-stats R-zoo
BuildRequires:    R-graphics R-stats R-sandwich R-zoo 


%description
Tools for the generalized logistic distribution (Type I, also known as
skew-logistic distribution), encompassing basic distribution functions (p,
q, d, r, score), maximum likelihood estimation, and structural change

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
%doc %{rlibdir}/glogis/html
%doc %{rlibdir}/glogis/NEWS
%doc %{rlibdir}/glogis/CITATION
%doc %{rlibdir}/glogis/DESCRIPTION
%{rlibdir}/glogis/NAMESPACE
%{rlibdir}/glogis/data
%{rlibdir}/glogis/help
%{rlibdir}/glogis/R
%{rlibdir}/glogis/INDEX
%{rlibdir}/glogis/demo
%{rlibdir}/glogis/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora