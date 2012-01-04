%global packname  RANN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.3
Release:          1%{?dist}
Summary:          Fast Nearest Neighbour Search

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Finds the k nearest neighbours for every point in a given dataset in O(N
log N) time using Arya and Mount's ANN library (v1.1.1).  Two functions
allow searches for nearest neighbours within a point set or between two
separate point sets. There is support for approximate as well as exact
searches, fixed radius searches and bd as well as kd trees. This version
updates ANN 1.1.3 and fixes package compilation on Windows.

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
%doc %{rlibdir}/RANN/html
%doc %{rlibdir}/RANN/DESCRIPTION
%{rlibdir}/RANN/R
%{rlibdir}/RANN/help
%{rlibdir}/RANN/INDEX
%{rlibdir}/RANN/NAMESPACE
%{rlibdir}/RANN/libs
%{rlibdir}/RANN/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.3-1
- initial package for Fedora