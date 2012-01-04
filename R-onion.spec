%global packname  onion
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          octonions and quaternions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of routines to manipulate and visualize quaternions and

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
%doc %{rlibdir}/onion/doc
%doc %{rlibdir}/onion/DESCRIPTION
%doc %{rlibdir}/onion/html
%{rlibdir}/onion/Meta
%{rlibdir}/onion/help
%{rlibdir}/onion/data
%{rlibdir}/onion/INDEX
%{rlibdir}/onion/R
%{rlibdir}/onion/libs
%{rlibdir}/onion/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora