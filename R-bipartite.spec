%global packname  bipartite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.17
Release:          1%{?dist}
Summary:          Visualising bipartite networks and calculating some (ecological) indices.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-methods R-tnet R-vegan 


BuildRequires:    R-devel tex(latex) R-MASS R-methods R-tnet R-vegan



%description
Bipartite provides functions to visualise webs and calculate a series of
indices commonly used to describe pattern in ecological webs. It focusses
on webs consisting of only two trophic levels, e.g. pollination webs or
predator-prey-webs. Visualisation is important to get an idea of what we
are actually looking at, while the indices summarise different aspects of
the webs topology.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.17-1
- initial package for Fedora