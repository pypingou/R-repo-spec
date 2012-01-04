%global packname  makesweave
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Literate Programming with Make and Sweave

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A package for using Make to build Sweave documents efficiently.

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
%doc %{rlibdir}/makesweave/DESCRIPTION
%doc %{rlibdir}/makesweave/html
%doc %{rlibdir}/makesweave/doc
%{rlibdir}/makesweave/NAMESPACE
%{rlibdir}/makesweave/help
%{rlibdir}/makesweave/INDEX
%{rlibdir}/makesweave/R
%{rlibdir}/makesweave/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora