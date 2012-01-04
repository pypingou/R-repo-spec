%global packname  robustbase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.8
Release:          1%{?dist}
Summary:          Basic Robust Statistics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics R-methods 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-methods 

%description
"Essential" Robust Statistics.  The goal is to provide tools allowing to
analyze data with robust methods.  This includes regression methodology
including model selections and multivariate statistics where we strive to
cover the book "Robust Statistics, Theory and Methods" by Maronna, Martin
and Yohai; Wiley 2006.

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
%doc %{rlibdir}/robustbase/doc
%doc %{rlibdir}/robustbase/DESCRIPTION
%doc %{rlibdir}/robustbase/html
%doc %{rlibdir}/robustbase/CITATION
%{rlibdir}/robustbase/mcnaive.R
%{rlibdir}/robustbase/data
%{rlibdir}/robustbase/NAMESPACE
%{rlibdir}/robustbase/help
%{rlibdir}/robustbase/libs
RPM build errors:
%{rlibdir}/robustbase/R
%{rlibdir}/robustbase/test_LTS.R
%{rlibdir}/robustbase/test_MCD.R
%{rlibdir}/robustbase/ex-funs.R
%{rlibdir}/robustbase/Meta
%{rlibdir}/robustbase/INDEX
%{rlibdir}/robustbase/Copyrights

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.8-1
- initial package for Fedora