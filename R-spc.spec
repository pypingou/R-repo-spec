%global packname  spc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Statistical Process Control

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Evaluation of control charts by means of the zero-state, steady-state ARL
(Average Run Length). Setting up control charts for given in-control ARL
and plotting of the related figures. The control charts under
consideration are one- and two-sided EWMA, CUSUM, and Shiryaev-Roberts
schemes for monitoring the mean of normally distributed independent data.
Now, the ARL calculation of the same set of schemes under drift are added.
Other charts and parameters are in preparation. Further SPC areas will be
covered as well (sampling plans, capability indices ...).

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
%doc %{rlibdir}/spc/html
%doc %{rlibdir}/spc/DESCRIPTION
%{rlibdir}/spc/Meta
%{rlibdir}/spc/libs
%{rlibdir}/spc/help
%{rlibdir}/spc/R
%{rlibdir}/spc/NAMESPACE
%{rlibdir}/spc/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora