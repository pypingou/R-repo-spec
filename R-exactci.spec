%global packname  exactci
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.0.1
Release:          1%{?dist}
Summary:          Exact P-values and Matching Confidence Intervals for simple Discrete Parametric Cases

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Calculates exact tests and confidence intervals for one-sample binomial
and one- or two-sample Poisson cases.

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
%doc %{rlibdir}/exactci/html
%doc %{rlibdir}/exactci/DESCRIPTION
%doc %{rlibdir}/exactci/doc
%doc %{rlibdir}/exactci/CITATION
%{rlibdir}/exactci/INDEX
%{rlibdir}/exactci/help
%{rlibdir}/exactci/Meta
%{rlibdir}/exactci/R
%{rlibdir}/exactci/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0.1-1
- initial package for Fedora