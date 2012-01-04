%global packname  DAAGxtras
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.2
Release:          1%{?dist}
Summary:          Data Sets and Functions, supplementary to DAAG

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
various data sets used in additional exercises for the book Maindonald,
J.H. and Braun, W.J. (3rd edn 2010) "Data Analysis and Graphics Using R",
and for a 'Data Mining' course. Note that a number of datasets that were
in version 0.7-6 of this package have been transferred to the DAAG

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
%doc %{rlibdir}/DAAGxtras/html
%doc %{rlibdir}/DAAGxtras/DESCRIPTION
%doc %{rlibdir}/DAAGxtras/doc
%{rlibdir}/DAAGxtras/data
%{rlibdir}/DAAGxtras/R
%{rlibdir}/DAAGxtras/Meta
%{rlibdir}/DAAGxtras/help
%{rlibdir}/DAAGxtras/NAMESPACE
%{rlibdir}/DAAGxtras/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.2-1
- initial package for Fedora