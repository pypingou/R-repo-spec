%global packname  dichromat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          Color schemes for dichromats

Group:            Applications/Engineering 
License:          GPL2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Collapse red-green distinctions to simulate the effects of

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
%doc %{rlibdir}/dichromat/DESCRIPTION
%doc %{rlibdir}/dichromat/html
%{rlibdir}/dichromat/INDEX
%{rlibdir}/dichromat/NAMESPACE
%{rlibdir}/dichromat/data
%{rlibdir}/dichromat/R
%{rlibdir}/dichromat/Meta
%{rlibdir}/dichromat/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora