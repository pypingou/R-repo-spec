%global packname  estrogen
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.7
Release:          1%{?dist}
Summary:          2x2 factorial design exercise for the Bioconductor short course

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy 


BuildRequires:    R-devel tex(latex) R-affy



%description
Data from 8 Affymetrix genechips, looking at a 2x2 factorial design (with
2 repeats per level)

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.7-1
- initial package for Fedora