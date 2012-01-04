%global packname  changeLOS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.9.2
Release:          1%{?dist}
Summary:          Change in LOS

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Change in length of hospital stay (LOS) is frequently used to assess the
impact and the costs of hospital-acquired complications. In order to
compute the attributable change in LOS, it is crucial to account for the
timing of events: A complication can only have an effect on LOS, once it
has occured. These temporal dynamics can be adequately handled by
multistate models; however, there is few software for such models
available. We introduce an R-package "changeLOS" for computing change in
LOS based on methods described in Schulgen and Schumacher (1996). We will
illustrate the program on data from a prospective cohort study on
hospital-acquired infections. Main features of the R-package "changeLOS"
are R-methods to: (1) describe the multi-state model. (2) compute the
Aalen-Johansen estimator for the matrix of transition probabilities P(u-,
u) for all observed transition times u.(3) compute the Aalen-Johansen
estimator for the matrix of transition probabilities P(s,t); the estimator
is a finite matrix product of matrices P(u-,u) for every observed event
time in the interval(s,t]. (4) visualize the temporal dynamics of the
data, illustrated by transition probabilities. (5) compute and visualize
change in LOS. (6) compute bootstrap variances for change in LOS.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.9.2-1
- initial package for Fedora