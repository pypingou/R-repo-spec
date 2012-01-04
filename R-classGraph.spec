%global packname  classGraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.4
Release:          1%{?dist}
Summary:          Construct Graphs of S4 Class Hierarchies

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graph R-Rgraphviz 
Requires:         R-methods R-graph R-Rgraphviz 

BuildRequires:    R-devel tex(latex) R-methods R-graph R-Rgraphviz
BuildRequires:    R-methods R-graph R-Rgraphviz 


%description
Construct directed graphs of S4 class hierarchies and visualize them.  In
general, these graphs typically are DAGs (directed acyclic graphs), often
simple trees in practice.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.4-1
- initial package for Fedora