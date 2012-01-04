%global packname  pdInfoBuilder
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18.0
Release:          1%{?dist}
Summary:          Platform Design Information Package Builder

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-Biobase R-RSQLite R-affxparser R-oligo 
Requires:         R-Biostrings R-IRanges 

BuildRequires:    R-devel tex(latex) R-methods R-Biobase R-RSQLite R-affxparser R-oligo
BuildRequires:    R-Biostrings R-IRanges 


%description
Builds platform design information packages. These consist of a SQLite
database containing feature-level data such as x, y position on chip and
featureSet ID. The database also incorporates featureSet-level annotation
data. The products of this packages are used by the oligo pkg.

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
* Sun Dec 11 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18.0-1
- initial package for Fedora