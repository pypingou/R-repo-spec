%global packname  ROracle
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.12
Release:          1%{?dist}
Summary:          Oracle database interface for R

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-DBI 
Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-DBI
BuildRequires:    R-utils 


%description
Oracle database interface (DBI) driver for R. This is a DBI-compliant
Oracle driver based on the ProC/C++ embedded SQL. It implements the DBI
version 0.1-8 plus one extension.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.12-1
- initial package for Fedora