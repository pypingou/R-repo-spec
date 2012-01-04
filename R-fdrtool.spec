%global packname  fdrtool
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.7
Release:          1%{?dist}
Summary:          Estimation and Control of (Local) False Discovery Rates

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package allows to estimate both tail area-based false discovery rates
(Fdr) as well as local false discovery rates (fdr) for a variety of null
models (p-values, z-scores, correlation coefficients, t-scores).  The
proportion of null values and the parameters of the null distribution are
adaptively estimated from the data.  In addition, the package contains
functions for non-parametric density estimation (Grenander estimator), for
monotone regression (isotonic regression and antitonic regression with
weights), for computing the greatest convex minorant (GCM) and the least
concave majorant (LCM), and for the half-normal and correlation

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
%doc %{rlibdir}/fdrtool/NEWS
%doc %{rlibdir}/fdrtool/html
%doc %{rlibdir}/fdrtool/DESCRIPTION
%{rlibdir}/fdrtool/help
%{rlibdir}/fdrtool/LICENSE
%{rlibdir}/fdrtool/INDEX
%{rlibdir}/fdrtool/Meta
%{rlibdir}/fdrtool/libs
%{rlibdir}/fdrtool/R
%{rlibdir}/fdrtool/data
%{rlibdir}/fdrtool/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.7-1
- initial package for Fedora