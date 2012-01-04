%global packname  simecol
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Simulation of ecological (and other) dynamic systems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-deSolve R-methods R-lattice 

BuildRequires:    R-devel tex(latex) R-deSolve R-methods R-lattice 

%description
simecol is an object oriented framework to simulate ecological (and other)
dynamic systems. It can be used for differential equations,
individual-based (or agent-based) and other models as well. The package
helps to organize scenarios (avoids copy and paste) and improves
readability and usability of code.

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
%doc %{rlibdir}/simecol/DESCRIPTION
%doc %{rlibdir}/simecol/CITATION
%doc %{rlibdir}/simecol/doc
%doc %{rlibdir}/simecol/html
%doc %{rlibdir}/simecol/NEWS
%{rlibdir}/simecol/NAMESPACE
%{rlibdir}/simecol/FAQ.txt
%{rlibdir}/simecol/Meta
%{rlibdir}/simecol/WISHLIST
%{rlibdir}/simecol/libs
%{rlibdir}/simecol/demo
%{rlibdir}/simecol/help
%{rlibdir}/simecol/R
%{rlibdir}/simecol/data
%{rlibdir}/simecol/THANKS
%{rlibdir}/simecol/ToDo.txt
%{rlibdir}/simecol/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora