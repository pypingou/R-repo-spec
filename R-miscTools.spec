%global packname  miscTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.12
Release:          1%{?dist}
Summary:          Miscellanneous Tools and Utilities

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-12.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Miscellanneous small tools and utilities

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
%doc %{rlibdir}/miscTools/html
%doc %{rlibdir}/miscTools/NEWS
%doc %{rlibdir}/miscTools/DESCRIPTION
%{rlibdir}/miscTools/R
%{rlibdir}/miscTools/Meta
%{rlibdir}/miscTools/help
%{rlibdir}/miscTools/INDEX
%{rlibdir}/miscTools/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.12-1
- initial package for Fedora