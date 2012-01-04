%global packname  SOAR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.8
Release:          1%{?dist}
Summary:          Memory management in R by delayed assignments

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.99-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Allows objects to be stored on disc and automatically recalled as required
into memory by delayed assignment.

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
%doc %{rlibdir}/SOAR/NEWS
%doc %{rlibdir}/SOAR/html
%doc %{rlibdir}/SOAR/doc
%doc %{rlibdir}/SOAR/DESCRIPTION
%{rlibdir}/SOAR/R
%{rlibdir}/SOAR/NAMESPACE
%{rlibdir}/SOAR/help
%{rlibdir}/SOAR/INDEX
%{rlibdir}/SOAR/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.8-1
- initial package for Fedora