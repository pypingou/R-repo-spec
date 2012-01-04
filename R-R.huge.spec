%global packname  R.huge
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Methods for accessing huge amounts of data [DEPRECATED]

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-R.oo R-R.utils 

BuildRequires:    R-devel tex(latex) R-R.oo R-R.utils 

%description
THIS PACKAGE HAS BEEN DEPRECATED. Do not start building new projects based
on it. Cross-platform alternatives are the following packages: bigmemory
(CRAN), ff (CRAN), BufferedMatrix (BioConductor).  The main usage of it
was inside the aroma.affymetrix package. (The package currently provides a
class representing a matrix where the actual data is stored in a binary
format on the local file system.  This way the size limit of the data is
set by the file system and not the memory.)

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
%doc %{rlibdir}/R.huge/DESCRIPTION
%doc %{rlibdir}/R.huge/NEWS
%doc %{rlibdir}/R.huge/html
%{rlibdir}/R.huge/R
%{rlibdir}/R.huge/INDEX
%{rlibdir}/R.huge/Meta
%{rlibdir}/R.huge/NAMESPACE
%{rlibdir}/R.huge/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora