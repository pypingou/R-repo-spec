%global packname  plgp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Particle Learning of Gaussian Processes

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-tgp 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-tgp 

%description
Sequential Monte Carlo inference for fully Bayesian Gaussian process (GP)
regression and classification models by particle learning (PL).  The
sequential nature of inference and the active learning (AL) hooks provided
facilitate thrifty sequential design (by entropy) and optimization (by
improvement) for classification and regression models, respectively. This
package essentially provides a generic PL interface, and functions
(arguments to the interface) which implement the GP models and AL
heuristics.  Functions for a special, linked, regression/classification GP
model and an integrated expected conditional improvement (IECI) statistic
is provides for optimization in the presence of unknown constraints.
Separable and isotropic Gaussian, and single-index correlation functions
are supported. See the examples section of ?plgp and demo(package="plgp")
for an index of demos

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
%doc %{rlibdir}/plgp/html
%doc %{rlibdir}/plgp/DESCRIPTION
%{rlibdir}/plgp/demo
%{rlibdir}/plgp/NAMESPACE
%{rlibdir}/plgp/INDEX
%{rlibdir}/plgp/help
%{rlibdir}/plgp/Meta
%{rlibdir}/plgp/LICENSE
%{rlibdir}/plgp/libs
%{rlibdir}/plgp/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora