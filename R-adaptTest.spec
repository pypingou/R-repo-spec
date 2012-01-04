%global packname  adaptTest
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Adaptive two-stage tests

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
The functions defined in this program serve for implementing adaptive
two-stage tests. Currently, four tests are included: Bauer and Koehne
(1994), Lehmacher and Wassmer (1999), Vandemeulebroecke (2006), and the
horizontal conditional error function. User-defined tests can also be
implemented. Reference: Vandemeulebroecke, An investigation of two-stage
tests, Statistica Sinica 2006.

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
%doc %{rlibdir}/adaptTest/DESCRIPTION
%doc %{rlibdir}/adaptTest/html
%{rlibdir}/adaptTest/NAMESPACE
%{rlibdir}/adaptTest/help
%{rlibdir}/adaptTest/INDEX
%{rlibdir}/adaptTest/R
%{rlibdir}/adaptTest/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora