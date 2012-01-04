%global packname  xgobi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.14
Release:          1%{?dist}
Summary:          Interface to the XGobi and XGvis programs for graphical data analysis

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Interface to the XGobi and XGvis programs for graphical data analysis.

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
%doc %{rlibdir}/xgobi/html
%doc %{rlibdir}/xgobi/DESCRIPTION
%{rlibdir}/xgobi/R
%{rlibdir}/xgobi/Meta
%{rlibdir}/xgobi/scripts
%{rlibdir}/xgobi/data
%{rlibdir}/xgobi/INSTALL.windows
%{rlibdir}/xgobi/INDEX
%{rlibdir}/xgobi/help
%{rlibdir}/xgobi/LICENSE
%{rlibdir}/xgobi/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.14-1
- initial package for Fedora