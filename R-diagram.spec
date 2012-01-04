%global packname  diagram
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.2
Release:          1%{?dist}
Summary:          Functions for visualising simple graphs (networks), plotting flow diagrams

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-shape 

BuildRequires:    R-devel tex(latex) R-shape 

%description
Visualises simple graphs (networks) based on a transition matrix,
utilities to plot flow diagrams, visualising webs,... Support for the book
"A practical guide to ecological modelling - using R as a simulation
platform" by Karline Soetaert and Peter M.J. Herman (2009). Springer.
Includes demo(flowchart), demo(plotmat), demo(plotweb)

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
%doc %{rlibdir}/diagram/html
%doc %{rlibdir}/diagram/doc
%doc %{rlibdir}/diagram/DESCRIPTION
%{rlibdir}/diagram/help
%{rlibdir}/diagram/NAMESPACE
%{rlibdir}/diagram/Meta
%{rlibdir}/diagram/R
%{rlibdir}/diagram/demo
%{rlibdir}/diagram/data
%{rlibdir}/diagram/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.2-1
- initial package for Fedora