%global packname  GillespieSSA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.4
Release:          1%{?dist}
Summary:          Gillespie's Stochastic Simulation Algorithm (SSA)

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
GillespieSSA provides a simple to use, intuitive, and extensible interface
to several stochastic simulation algorithms for generating simulated
trajectories of finite population continuous-time model. Currently it
implements Gillespie's exact stochastic simulation algorithm (Direct
method) and several approximate methods (Explicit tau-leap, Binomial
tau-leap, and Optimized tau-leap). The package also contains a library of
template models that can be run as demo models and can easily be
customized and extended. Currently the following models are included,
decaying-dimerization reaction set, linear chain system, logistic growth
model, Lotka predator-prey model, Rosenzweig-MacArthur predator-prey
model, Kermack-McKendrick SIR model, and a metapopulation SIRS model.

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
%doc %{rlibdir}/GillespieSSA/doc
%doc %{rlibdir}/GillespieSSA/html
%doc %{rlibdir}/GillespieSSA/DESCRIPTION
%{rlibdir}/GillespieSSA/help
RPM build errors:
%{rlibdir}/GillespieSSA/INDEX
%{rlibdir}/GillespieSSA/R
%{rlibdir}/GillespieSSA/demo
%{rlibdir}/GillespieSSA/Meta
%{rlibdir}/GillespieSSA/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.4-1
- initial package for Fedora