%global packname  WWGbook
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Functions and datasets for WWGbook.

Group:            Applications/Engineering 
License:          GPL (version 2 or later)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Book is "Linear Mixed Models: A Practical Guide Using Statistical
Software" published in 2006 by Chapman Hall / CRC Press

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
%doc %{rlibdir}/WWGbook/DESCRIPTION
%doc %{rlibdir}/WWGbook/LICENCE
%doc %{rlibdir}/WWGbook/CITATION
%doc %{rlibdir}/WWGbook/NEWS
%doc %{rlibdir}/WWGbook/html
%{rlibdir}/WWGbook/help
%{rlibdir}/WWGbook/INDEX
%{rlibdir}/WWGbook/scripts
%{rlibdir}/WWGbook/data
%{rlibdir}/WWGbook/NAMESPACE
%{rlibdir}/WWGbook/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora