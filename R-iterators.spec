%global packname  iterators
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Iterator construct for R

Group:            Applications/Engineering 
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Support for iterators, which allow a programmer to traverse through all
the elements of a vector, list, or other collection of data.

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
%doc %{rlibdir}/iterators/html
%doc %{rlibdir}/iterators/DESCRIPTION
%doc %{rlibdir}/iterators/doc
%{rlibdir}/iterators/R
%{rlibdir}/iterators/Meta
%{rlibdir}/iterators/help
%{rlibdir}/iterators/unitTests
%{rlibdir}/iterators/INDEX
%{rlibdir}/iterators/examples
%{rlibdir}/iterators/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora