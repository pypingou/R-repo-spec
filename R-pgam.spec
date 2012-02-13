%global packname  pgam
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.12
Release:          1%{dist}
Summary:          Poisson-Gamma Additive Models.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-utils 

BuildRequires:    R-devel tex(latex) R-stats R-utils 

%description
This work is an extension of the state space model for Poisson count data,
Poisson-Gamma model, towards a semiparametric specification. Just like the
generalized additive models (GAM), cubic splines are used for covariate
smoothing. The semiparametric models are fitted by an iterative process
that combines maximization of likelihood and backfitting algorithm.

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
%doc %{rlibdir}/pgam/html
%doc %{rlibdir}/pgam/DESCRIPTION
%{rlibdir}/pgam/NAMESPACE
%{rlibdir}/pgam/INDEX
%{rlibdir}/pgam/R
%{rlibdir}/pgam/help
%{rlibdir}/pgam/data
%{rlibdir}/pgam/libs
%{rlibdir}/pgam/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.12-1
- Update to version 0.4.12

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.11-1
- initial package for Fedora