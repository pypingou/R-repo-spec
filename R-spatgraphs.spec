%global packname  spatgraphs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.44
Release:          1%{?dist}
Summary:          Graphs for spatial point patterns

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Graphs, graph visualization and graph component calculations, ment to be
used as a tool in spatial point pattern analysis. See package 'spatstat'
for more info about spatial point patterns.

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
%doc %{rlibdir}/spatgraphs/DESCRIPTION
%doc %{rlibdir}/spatgraphs/html
%{rlibdir}/spatgraphs/R
%{rlibdir}/spatgraphs/libs
%{rlibdir}/spatgraphs/Meta
%{rlibdir}/spatgraphs/NAMESPACE
%{rlibdir}/spatgraphs/help
%{rlibdir}/spatgraphs/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.44-1
- initial package for Fedora