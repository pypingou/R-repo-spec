%global packname  chopsticks
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.1
Release:          1%{?dist}
Summary:          The snp.matrix and X.snp.matrix classes

Group:            Applications/Engineering 
License:          GNU General Public Licence (GPLv3)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-methods 

BuildRequires:    R-devel tex(latex) R-survival R-methods 

%description
Implements classes and methods for large-scale SNP association studies

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.1-1
- initial package for Fedora