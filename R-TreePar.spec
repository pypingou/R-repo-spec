%global packname  TreePar
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2
Release:          1%{?dist}
Summary:          Estimating speciation and extinction rates based on phylogenies

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ape R-Matrix R-subplex R-TreeSim 


BuildRequires:    R-devel tex(latex) R-ape R-Matrix R-subplex R-TreeSim



%description
For a given species phylogeny on present day data which is calibrated to
calendar-time, a method for estimating maximum likelihood speciation and
extinction processes is provided. The method allows for non-constant
rates. Rates may change (i) as a function of time, i.e. rate shifts at
specified times or mass extinction events (implemented as bd.shifts.optim)
or (ii) as a function of the number of species, i.e. density-dependence
(implemented as bd.densdep.optim). Note that the method takes into account
the whole phylogeny, in particular it accounts for the "pull of the
present" effect. For a given phylogeny on higher taxa, but where the
number of species is known within each higher taxa, speciation and
extinction rates can be estimated, under the assumption that these rates
remained constant (implemented as bd.groups.optim).

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2-1
- initial package for Fedora