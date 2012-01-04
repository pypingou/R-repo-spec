%global packname  sp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.91
Release:          1%{?dist}
Summary:          classes and methods for spatial data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-91.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A package that provides classes and methods for spatial data. The classes
document where the spatial location information resides, for 2D or 3D
data. Utility functions are provided, e.g. for plotting data as maps,
spatial selection, as well as methods for retrieving coordinates, for
subsetting, print, summary, etc.

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
%doc %{rlibdir}/sp/DESCRIPTION
%doc %{rlibdir}/sp/html
%doc %{rlibdir}/sp/doc
%doc %{rlibdir}/sp/CITATION
%{rlibdir}/sp/R
%{rlibdir}/sp/demo
%{rlibdir}/sp/include
%{rlibdir}/sp/NAMESPACE
%{rlibdir}/sp/INDEX
%{rlibdir}/sp/ChangeLog
%{rlibdir}/sp/Meta
RPM build errors:
%{rlibdir}/sp/help
%{rlibdir}/sp/libs
%{rlibdir}/sp/data
%{rlibdir}/sp/external

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.91-1
- initial package for Fedora