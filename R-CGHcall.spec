%global packname  CGHcall
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.14.0
Release:          1%{?dist}
Summary:          Calling aberrations for array CGH tumor profiles.

Group:            Applications/Engineering 
License:          GPL (http://www.gnu.org/copyleft/gpl.html)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-impute R-DNAcopy R-methods R-Biobase R-CGHbase 

BuildRequires:    R-devel tex(latex) R-impute R-DNAcopy R-methods R-Biobase R-CGHbase 

%description
Calls aberrations for array CGH data using a six state mixture model as
well as several biological concepts that are ignored by existing
algorithms. Visualization of profiles is also provided.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.14.0-1
- initial package for Fedora