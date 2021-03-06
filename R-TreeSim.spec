%global packname  TreeSim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Simulating trees under the birth-death model

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ape R-geiger 


BuildRequires:    R-devel tex(latex) R-ape R-geiger



%description
The package simulates phylogenetic trees under a constant-rate birth-death
process, conditioned on having a fixed number of final tips (sim.bd.taxa),
or a fixed age (sim.bd.age), or a fixed age and number of tips
(sim.bd.taxa.age). When conditioning on the number of final tips, the
method allows for shifts in rates and mass extinction events during the
birth-death process (sim.rateshift.taxa). When fixing on the age, the
method further allows the speciation rate to change in a density-dependent
way (sim.bd.age), and one can plot the average LTT plot
(LTT.average.root). TreeSim further samples appropriately trees with n
final tips from a set of trees generated by the common sampling algorithm
stopping when a fixed number m>>n of leaves is first reached
(bd.gsa.taxa). This latter method is appropriate for m-tip trees generated
under a big class of models (details in the bd.gsa.taxa man page). For
incomplete phylogeny, the missing speciation events can be added through
simulations (corsim).

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora