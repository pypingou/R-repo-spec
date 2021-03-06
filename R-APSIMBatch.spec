%global packname  APSIMBatch
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0.2374
Release:          1%{?dist}
Summary:          Analysis the output of Apsim software

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Run APSIM in Batch mode

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
%doc %{rlibdir}/APSIMBatch/DESCRIPTION
%doc %{rlibdir}/APSIMBatch/html
%{rlibdir}/APSIMBatch/R
%{rlibdir}/APSIMBatch/Meta
%{rlibdir}/APSIMBatch/help
%{rlibdir}/APSIMBatch/INDEX
%{rlibdir}/APSIMBatch/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0.2374-1
- initial package for Fedora