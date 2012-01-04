%global packname  BayHap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Bayesian analysis of haplotype association using Markov Chain Monte Carlo

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boa 


BuildRequires:    R-devel tex(latex) R-boa



%description
The package BayHap performs simultaneous estimation of uncertain haplotype
frequencies and association with haplotypes based on generalized linear
models for quantitative, binary and survival traits. Bayesian statistics
and Markov Chain Monte Carlo techniques are the theoretical framework for
the methods of estimation included in this package. Prior values for model
parameters can be included by the user. Convergence diagnostics and
statistical and graphical analysis of the sampling output can be also
carried out.

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
%doc %{rlibdir}/BayHap/DESCRIPTION
%doc %{rlibdir}/BayHap/html
%{rlibdir}/BayHap/libs
RPM build errors:
%{rlibdir}/BayHap/Meta
%{rlibdir}/BayHap/help
%{rlibdir}/BayHap/R
%{rlibdir}/BayHap/INDEX
%{rlibdir}/BayHap/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora