%global packname  hmm.discnp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.5
Release:          1%{?dist}
Summary:          Hidden Markov models with discrete non-parametric observation distributions.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Fits hidden Markov models with discrete non-parametric observation
distributions to data sets.  Simulates data from such models.  Finds most
probable underlying hidden states, the most probable sequences of such
states, and the log likelihood of a collection of observations given the
parameters of the model.

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
%doc %{rlibdir}/hmm.discnp/DESCRIPTION
%doc %{rlibdir}/hmm.discnp/html
%{rlibdir}/hmm.discnp/Ratfor
%{rlibdir}/hmm.discnp/INDEX
%{rlibdir}/hmm.discnp/READ_ME
%{rlibdir}/hmm.discnp/NAMESPACE
%{rlibdir}/hmm.discnp/libs
%{rlibdir}/hmm.discnp/Meta
%{rlibdir}/hmm.discnp/R
%{rlibdir}/hmm.discnp/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.5-1
- initial package for Fedora