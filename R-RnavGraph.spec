%global packname  RnavGraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Using graphs as a navigational infrastructure.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-tcltk R-graph 
Requires:         R-RBGL 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-tcltk R-graph
BuildRequires:    R-RBGL 


%description
GUI to explore high dimensional data (including image data) using graphs
as navigational infrastructure.

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
%doc %{rlibdir}/RnavGraph/NEWS
%doc %{rlibdir}/RnavGraph/html
%doc %{rlibdir}/RnavGraph/DESCRIPTION
%doc %{rlibdir}/RnavGraph/doc
%{rlibdir}/RnavGraph/help
%{rlibdir}/RnavGraph/tcl
%{rlibdir}/RnavGraph/NAMESPACE
%{rlibdir}/RnavGraph/demo
%{rlibdir}/RnavGraph/data
%{rlibdir}/RnavGraph/libs
%{rlibdir}/RnavGraph/Meta
%{rlibdir}/RnavGraph/R
%{rlibdir}/RnavGraph/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora