%global packname  rsbml
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.12.0
Release:          1%{?dist}
Summary:          R support for SBML, using libsbml

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils 
Requires:         R-graph R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils
BuildRequires:    R-graph R-utils 


%description
Links R to libsbml for SBML parsing, validating output, provides an S4
SBML DOM, converts SBML to R graph objects. Optionally links to the SBML
ODE Solver Library (SOSLib) for simulating models.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12.0-1
- initial package for Fedora