%global packname  network
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7
Release:          1%{?dist}
Summary:          Classes for Relational Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Tools to create and modify network objects.  The network class can
represent a range of relational data types, and supports arbitrary
vertex/edge/graph attributes.

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
%doc %{rlibdir}/network/html
%doc %{rlibdir}/network/CITATION
%doc %{rlibdir}/network/DESCRIPTION
%{rlibdir}/network/network.api
%{rlibdir}/network/INDEX
%{rlibdir}/network/libs
%{rlibdir}/network/help
%{rlibdir}/network/Meta
%{rlibdir}/network/data
%{rlibdir}/network/R
%{rlibdir}/network/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7-1
- initial package for Fedora