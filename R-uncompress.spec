%global packname  uncompress
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.34
Release:          1%{?dist}
Summary:          Uncompress

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This R Add-On provides the function uncompress(raw) for decompressing .Z
files.  It returns the decompressed data as a raw (binary) string.  The
compressed data is passed in in the same format.  It returns NULL if the
input data is invalid.

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
%doc %{rlibdir}/uncompress/DESCRIPTION
%doc %{rlibdir}/uncompress/html
%{rlibdir}/uncompress/NAMESPACE
%{rlibdir}/uncompress/INDEX
%{rlibdir}/uncompress/help
%{rlibdir}/uncompress/Meta
RPM build errors:
%{rlibdir}/uncompress/R
%{rlibdir}/uncompress/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.34-1
- initial package for Fedora