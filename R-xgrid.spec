%global packname  xgrid
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.11
Release:          1%{?dist}
Summary:          Access Apple Xgrid using R

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions to distribute and collate results from simulation studies and
other computationally expensive tasks to Apple Xgrid clusters from within

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
%doc %{rlibdir}/xgrid/DESCRIPTION
%doc %{rlibdir}/xgrid/doc
%doc %{rlibdir}/xgrid/html
%{rlibdir}/xgrid/INDEX
%{rlibdir}/xgrid/NAMESPACE
%{rlibdir}/xgrid/help
%{rlibdir}/xgrid/R
%{rlibdir}/xgrid/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.11-1
- initial package for Fedora