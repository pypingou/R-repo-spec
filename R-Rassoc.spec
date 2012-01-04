%global packname  Rassoc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.03
Release:          1%{?dist}
Summary:          Robust tests for case-control genetic association studies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package supplies several robust tests for case-control genetic
association studies. The tests contained in this package are: allelic
based test, Cochran-Armitage trend test, maximin efficiency robust test,
MAX3 test and genetic model selection test. For each test, the
corresponding R code reports the test statistics and the associated

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
%doc %{rlibdir}/Rassoc/CITATION
%doc %{rlibdir}/Rassoc/DESCRIPTION
%doc %{rlibdir}/Rassoc/html
%{rlibdir}/Rassoc/help
%{rlibdir}/Rassoc/INDEX
%{rlibdir}/Rassoc/NAMESPACE
%{rlibdir}/Rassoc/Meta
%{rlibdir}/Rassoc/data
%{rlibdir}/Rassoc/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.03-1
- initial package for Fedora