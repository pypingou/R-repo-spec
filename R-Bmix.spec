%global packname  Bmix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Bayesian Sampling for Stick-breaking Mixtures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This is a bare-bones implementation of sampling algorithms for a variety
of Bayesian stick-breaking (marginally DP) mixture models, including
particle learning and Gibbs sampling for static DP mixtures, particle
learning for dynamic BAR stick-breaking, and DP mixture regression. The
software is designed to be easy to customize to suit different situations
and for experimentation with stick-breaking models.  Since particles are
repeatedly copied, it is not an especially efficient implementation.

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
%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora