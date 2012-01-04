%global packname  x12
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          X12 - wrapper function and GUI

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tcltk R-stats R-utils R-grDevices 

BuildRequires:    R-devel tex(latex) R-tcltk R-stats R-utils R-grDevices 

%description
A wrapper function and GUI for the X12 binaries

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
%doc %{rlibdir}/x12/DESCRIPTION
%doc %{rlibdir}/x12/doc
%doc %{rlibdir}/x12/html
%{rlibdir}/x12/Meta
%{rlibdir}/x12/help
%{rlibdir}/x12/R
%{rlibdir}/x12/data
RPM build errors:
%{rlibdir}/x12/NAMESPACE
%{rlibdir}/x12/INDEX
%{rlibdir}/x12/tcl

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora