%global packname  GGMselect
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Gaussian Graphs Models selection

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-lars R-gtools 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-lars R-gtools 

%description
GGMselect is a package dedicated to graph estimation in Gaussian Graphical
Models. The main functions return the adjacency matrix of an undirected
graph estimated from a data matrix.

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
%doc %{rlibdir}/GGMselect/CITATION
%doc %{rlibdir}/GGMselect/doc
%doc %{rlibdir}/GGMselect/NEWS
%doc %{rlibdir}/GGMselect/DESCRIPTION
%doc %{rlibdir}/GGMselect/html
%{rlibdir}/GGMselect/INDEX
%{rlibdir}/GGMselect/Meta
%{rlibdir}/GGMselect/help
%{rlibdir}/GGMselect/R
RPM build errors:
%{rlibdir}/GGMselect/libs
%{rlibdir}/GGMselect/NAMESPACE
%{rlibdir}/GGMselect/demo

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora