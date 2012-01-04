%global packname  fishmethods
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          Fisheries Methods and Models in R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot R-stats R-foreign 

BuildRequires:    R-devel tex(latex) R-boot R-stats R-foreign 

%description
Fishery methods and models from Quinn and Deriso (1999), Haddon(2001) ,
and literature.

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
%doc %{rlibdir}/fishmethods/DESCRIPTION
%doc %{rlibdir}/fishmethods/html
%{rlibdir}/fishmethods/help
%{rlibdir}/fishmethods/NAMESPACE
%{rlibdir}/fishmethods/Meta
%{rlibdir}/fishmethods/R
%{rlibdir}/fishmethods/data
%{rlibdir}/fishmethods/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora