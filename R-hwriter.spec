%global packname  hwriter
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          HTML Writer - Outputs R objects in HTML format

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Easy-to-use and versatile functions to output R objects in HTML format

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
%doc %{rlibdir}/hwriter/DESCRIPTION
%doc %{rlibdir}/hwriter/html
%doc %{rlibdir}/hwriter/doc
%{rlibdir}/hwriter/Meta
%{rlibdir}/hwriter/R
%{rlibdir}/hwriter/images
%{rlibdir}/hwriter/scripts
%{rlibdir}/hwriter/help
%{rlibdir}/hwriter/NAMESPACE
%{rlibdir}/hwriter/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora