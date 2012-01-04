%global packname  iRefR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.93
Release:          1%{?dist}
Summary:          iRefIndex Manager

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graph R-RBGL R-igraph 

BuildRequires:    R-devel tex(latex) R-graph R-RBGL R-igraph 

%description
"iRefR" allows the user to load any version of the consolidated protein
interaction database "iRefIndex" and perform tasks such as: selecting
databases, pmids, experimental methods, searching for specific proteins,
separate binary interactions from complexes and polymers, generate
complexes according to an algorithm that looks after possible
binary-represented complexes, make general database statistics and create
network graphs, among others.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.93-1
- initial package for Fedora