%global packname  affyILM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.1
Release:          1%{?dist}
Summary:          Linear Model of background subtraction and the Langmuir isotherm

Group:            Applications/Engineering 
License:          GPL version 3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-affxparser R-gcrma R-affy R-graphics R-methods R-Biobase 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-affxparser R-gcrma R-affy R-graphics R-methods R-Biobase 


%description
affyILM is a preprocessing tool which estimates gene expression levels for
Affymetrix Gene Chips. Input from physical chemistry is employed to first
background subtract intensities before calculating concentrations on
behalf of the Langmuir model.

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
* Mon Dec 12 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.1-1
- initial package for Fedora