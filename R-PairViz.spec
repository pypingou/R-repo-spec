%global packname  PairViz
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.1
Release:          1%{dist}
Summary:          Visualization using Eulerian tours and Hamiltonian decompositions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-TSP R-gtools R-graph R-methods 

BuildRequires:    R-devel tex(latex) R-TSP R-gtools R-graph R-methods 

%description
Eulerian tours and Hamiltonian decompositions of complete graphs are used
to ameliorate order effects in statistical graphics.

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
%doc %{rlibdir}/PairViz/html
%doc %{rlibdir}/PairViz/DESCRIPTION
%{rlibdir}/PairViz/help
%{rlibdir}/PairViz/NAMESPACE
%{rlibdir}/PairViz/Meta
%{rlibdir}/PairViz/R
%{rlibdir}/PairViz/demo
%{rlibdir}/PairViz/data
%{rlibdir}/PairViz/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.1-1
- Update to version 1.2.1

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora