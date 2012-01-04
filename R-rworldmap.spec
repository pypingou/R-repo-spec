%global packname  rworldmap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1211
Release:          1%{?dist}
Summary:          For mapping global data : rworldmap

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-maptools R-foreign R-fields R-spam R-maps 

BuildRequires:    R-devel tex(latex) R-sp R-maptools R-foreign R-fields R-spam R-maps 

%description
Enables mapping of country level and gridded user datasets.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1211-1
- initial package for Fedora