%global packname  Imap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.32
Release:          1%{?dist}
Summary:          Interactive Mapping

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Zoom in and out of maps or any supplied lines or points, with control for
color, poly fill, and aspect.

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
%doc %{rlibdir}/Imap/html
%doc %{rlibdir}/Imap/DESCRIPTION
%{rlibdir}/Imap/NAMESPACE
%{rlibdir}/Imap/help
%{rlibdir}/Imap/Meta
%{rlibdir}/Imap/INDEX
%{rlibdir}/Imap/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32-1
- initial package for Fedora