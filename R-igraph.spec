%global packname  igraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.5.3
Release:          1%{?dist}
Summary:          Network analysis and visualization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5.5-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Routines for simple graphs and network analysis. igraph can handle large
graphs very well and provides functions for generating random and regular
graphs, graph visualization, centrality indices and much more.

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
%doc %{rlibdir}/igraph/CITATION
%doc %{rlibdir}/igraph/DESCRIPTION
%doc %{rlibdir}/igraph/html
%{rlibdir}/igraph/R
%{rlibdir}/igraph/libs
%{rlibdir}/igraph/help
%{rlibdir}/igraph/html_library.tcl
%{rlibdir}/igraph/NAMESPACE
%{rlibdir}/igraph/tkigraph_help
%{rlibdir}/igraph/igraph.gif
%{rlibdir}/igraph/Meta
%{rlibdir}/igraph/html_library.license.terms
%{rlibdir}/igraph/LICENSE
RPM build errors:
%{rlibdir}/igraph/my_html_library.tcl
%{rlibdir}/igraph/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.5.3-1
- initial package for Fedora